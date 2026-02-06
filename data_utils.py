# filepath:\Users\Judah\Desktop\CS-School\PythonFunda\data_utils.py
def process_sensor_data(raw_data, **config):
    # raw_data = list of readings
    # config options:
    # remove_outliers=True (discard >3σ from mean)
    # smooth=True (3-point moving average)
    # scale="normalize" or "standardize"
    # Unknown options → ignore

    Data = list(raw_data)

    def Mean(Values):
        return sum(Values) / len(Values)

    def StdAndMean(Values):
        MeanValue = Mean(Values)
        Variance = sum((Value - MeanValue) ** 2 for Value in Values) / len(Values)
        StandardDeviation = Variance ** 0.5
        return StandardDeviation, MeanValue

    if config.get("remove_outliers", False) and len(Data) > 0:
        StandardDeviation, MeanValue = StdAndMean(Data)
        if StandardDeviation > 0:
            FilteredValues = []
            for Value in Data:
                if abs(Value - MeanValue) <= 3 * StandardDeviation:
                    FilteredValues.append(Value)
            Data = FilteredValues
        # if std == 0, all values are identical and therefore there is nothing to remove

    if config.get("smooth", False) and len(Data) >= 3:
        SmoothedValues = []
        DataLength = len(Data)
        for Index in range(DataLength):
            if Index == 0:
                AverageValue = (Data[0] + Data[1]) / 2
            elif Index == DataLength - 1:
                AverageValue = (Data[-1] + Data[-2]) / 2
            else:
                AverageValue = (Data[Index - 1] + Data[Index] + Data[Index + 1]) / 3 # account for all neighbors since in the middle, had to play with this until it worked
            SmoothedValues.append(AverageValue)
        Data = SmoothedValues

    ScaleMode = config.get("scale", None)

    if ScaleMode == "normalize" and len(Data) > 0:
        MinValue = min(Data)
        MaxValue = max(Data)
        if MaxValue != MinValue:
            Data = [(Value - MinValue) / (MaxValue - MinValue) for Value in Data]
        else:
            Data = [0.0 for Value in Data]

    elif ScaleMode == "standardize" and len(Data) > 0:
        StandardDeviation, MeanValue = StdAndMean(Data)
        if StandardDeviation > 0:
            Data = [(Value - MeanValue) / StandardDeviation for Value in Data]
        else:
            Data = [0.0 for Value in Data]

    return Data

# Note to grader - Used AI to assist in explaining the funciton mean, variance, and std_dev as said in the announcement. 
# Had trouble at first understanding how to calculate std deviation and variance so I used AI to break it down for me.