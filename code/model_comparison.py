def plotSuccess():
    s = pd.Series(methodDict) # Convert the methodDict dictionary to a pandas Series
    s = s.sort_values(ascending=True) # Sort the series in ascending order
    plt.figure(figsize=(8,4))

    # Define colors for each bar
    colors = ["#F8B195", "#F67280", "#C06C84", "#6C5B7B", "#355C7D"]

    ax = s.plot(kind='barh', color = colors) # Plot the sorted series as horizontal bar chart

    # Add value labels to each bar
    for p in ax.patches:
        ax.annotate(str(round(p.get_width(), 2)), (p.get_width() * 1.005, p.get_y() + p.get_height() / 2),
                    ha='left', va='center', fontsize=7)

    plt.xlabel('Percentage')
    plt.ylabel('Model')
    plt.title('Bar plot showing the accuracy of each model')
    plt.show()

plotSuccess()
