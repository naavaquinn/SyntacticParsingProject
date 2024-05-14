gentle_right_Y = [1] * len(gentle_right)
gentle_wrong_Y = [0] * len(gentle_wrong)

gentle_X = gentle_right + gentle_wrong
gentle_Y = gentle_right_Y + gentle_wrong_Y
#reference for indices
#0: token index
#1: token
#2: pos
#3: head index
#4: dependency relation

def get_features(data_X):

  postags = set()
  tokenpos2headpos = set()
  tokenpos2headpos_deprel = set()

  for i in range(len(data_X)):
    for j in range(len(data_X[i])):
      postags.add(data_X[i][j][2])
      head_index = int(data_X[i][j][3])-1
      if head_index != -1:
        rel = data_X[i][j][2] + ":" + data_X[i][head_index][2]
        tokenpos2headpos.add(rel)
        labeled_rel = data_X[i][j][2] + ":" + data_X[i][j][4] + ":" + data_X[i][head_index][2]
        tokenpos2headpos_deprel.add(labeled_rel)
      else:
        rel = data_X[i][j][2] + ":" + "root_pos"
        tokenpos2headpos.add(rel)
        labeled_rel = data_X[i][j][2] + ":" + data_X[i][j][4] + ":" + "root_pos"
        tokenpos2headpos_deprel.add(labeled_rel)

  pos_list = sorted(postags)
  tokenpos2headpos_list = sorted(tokenpos2headpos)
  tokenpos2headpos_deprel_list = sorted(tokenpos2headpos_deprel)

  feature_columns = pos_list + tokenpos2headpos_list + tokenpos2headpos_deprel_list

  return feature_columns

feature_columns = get_features(gentle_train_X)
def extract_feature_counts(data_X, features):

  df = pd.DataFrame(0, index=range(len(data_X)), columns=features)

  for i in range(len(data_X)):
    for j in range(len(data_X[i])):
      feature_name_1 = data_X[i][j][2]
      head_index = int(data_X[i][j][3])-1
      if head_index != -1:
        feature_name_2 = data_X[i][j][2] + ":" + data_X[i][head_index][2]
        feature_name_3 = data_X[i][j][2] + ":" + data_X[i][j][4] + ":" + data_X[i][head_index][2]
      else:
        feature_name_2 = data_X[i][j][2] + ":" + "root_pos"
        feature_name_3 = data_X[i][j][2] + ":" + data_X[i][j][4] + ":" + "root_pos"
      if feature_name_1 in df.columns:
        df.at[i, feature_name_1] += 1
      if feature_name_2 in df.columns:
        df.at[i, feature_name_2] += 1
      if feature_name_3 in df.columns:
        df.at[i, feature_name_3] += 1

  return df

train_df = extract_feature_counts(gentle_train_X, feature_columns)
test_df = extract_feature_counts(gentle_test_X, feature_columns)
XY_train_df = train_df.assign(CLASS_TAGS=gentle_train_Y)
XY_test_df = test_df.assign(CLASS_TAGS=gentle_test_Y)

XY_train_df.to_pickle('train_data.pkl')
XY_test_df.to_pickle('test_data.pkl')
     
