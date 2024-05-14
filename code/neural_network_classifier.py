
X_train= np.concatenate((train_X, test_X))
Y_train= np.concatenate((train_Y, test_Y))
     

# Convert lists to NumPy arrays
array_train_X = np.array(X_train)
array_train_Y = np.array(Y_train)
     

model = Sequential([
Dense(16, input_shape=(1382,), activation='relu', kernel_regularizer=regularizers.l2(0.01)),
        Dropout(0.5),
        Dense(16, activation='relu', kernel_regularizer=regularizers.l2(0.01)),
        Dropout(0.5),
        Dense(1, activation='sigmoid')
])
     

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy', Precision(), Recall(), AUC()])
     

model.fit(array_train_X, array_train_Y, epochs=20, batch_size=32, validation_split=0.2)
scores = model.evaluate(array_train_X, array_train_Y, verbose=0)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

cvscores = []
cvscores.append(scores[1] * 100)

print("%.2f%% (+/- %.2f%%)" % (np.mean(cvscores), np.std(cvscores)))
     
