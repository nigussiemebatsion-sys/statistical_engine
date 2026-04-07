class StatEngine:
    def __init__(self, data):
        self.data = data

    def _clean_data(self):
        cleaned = []
        for i in self.data:
            if isinstance(i, (int, float)):
                cleaned.append(i)
            else:
                raise TypeError("All elements must be numbers")
        if len(cleaned) == 0:
            raise ValueError("Data cannot be empty")
        return cleaned

    """ mean is the average of the data points, 
    calculated by summing all the data points and dividing by the number of data or elements in the data set."""
    def get_mean(self):
        data = self._clean_data()
        total = 0
        for num in data:
            total += num
        return total / len(data)

    """ median is the middle value when the data is sorted.
    if the number of data points is odd, the median is the value at the middle index.
    if the number of data points is even, the median is the average of the middle two values."""
    def get_median(self):
        data = self._clean_data()
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 == 1:  # for odd number of elements
            return sorted_data[n // 2]
        else:  # for even number of elements
            return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2

    """mode is the value that appears most frequently in the data set.
    there can be more than one mode if multiple values have the same highest frequency."""
    def get_mode(self):
        data = self._clean_data()
        frequency = {}
        for number in data:
            frequency[number] = frequency.get(number, 0) + 1
        max_freq = max(frequency.values())
        solution = [num for num, freq in frequency.items() if freq == max_freq]
        return solution

    """ variance measures the average squared deviation of each data point from the mean. 
    it quantifies the spread of the data points around the mean.
    To calculate it, subtract the mean from each value, square the result, sum all these squared differences, and then divide by the total number of values."""       
    def get_variance(self, is_sample=True):
        data = self._clean_data()
        mean = self.get_mean()
        squared_deviations = [(x - mean) ** 2 for x in data]
        if is_sample:
            return sum(squared_deviations) / (len(data) - 1)
        else:
            return sum(squared_deviations) / len(data)

    """ standard deviation is simply the square root of the variance.
    to calculate it first calculate the variance and then take the square root of the variance."""
    def get_standard_deviation(self, is_sample=True):
        variance = self.get_variance(is_sample)
        return variance ** 0.5

    """ outlier: to calculate it first calculate the mean and standard deviation of the data set.
    then determine a threshold value by multiplying the standard deviation by a factor, in this case threshold is 2.
    if any values in the data fall outside the range of mean plus or minus the threshold value, they are considered outliers."""
    def get_outliers(self, threshold=2):
        data = self._clean_data()
        mean = self.get_mean()
        stand_dev = self.get_standard_deviation()
        return [x for x in data if abs(x - mean) > threshold * stand_dev]