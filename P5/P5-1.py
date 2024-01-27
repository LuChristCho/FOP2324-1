class MrCrab:
    def __init__(self, input_string):
        self.data = input_string

    def process_data(self):
        if self.data.startswith("m"):
            self.data += self.data[:10]
            self.data = self.data.replace("tt", "o")
        else:
            reversed_data = self.data[::-1]
            if reversed_data.startswith("m"):
                self.data = reversed_data.replace("tt", "o")
                self.data += self.data[:10]
            else:
                self.data = None

    def print_output(self):
        if self.data is not None:
            print(self.data)


class SpongeBob:
    def __init__(self, input_string):
        self.data = input_string

    def repeat_first_ten_characters(self):
        self.data += self.data[:10]

    def merge_sort(self, array):
        if len(array) > 1:
            mid = len(array) // 2
            left_half = array[:mid]
            right_half = array[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    array[k] = left_half[i]
                    i += 1
                else:
                    array[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                array[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                array[k] = right_half[j]
                j += 1
                k += 1

    def process_data(self):
        self.repeat_first_ten_characters()

        if self.data is not None and self.data.startswith("sb"):
            length_str = str(len(self.data))
            length_array = list(length_str)
            self.merge_sort(length_array)
            self.data = ''.join(map(str, length_array))
        else:
            self.data = None

    def print_output(self):
        if self.data is not None:
            print(self.data)



class Octopus:
    def __init__(self, input_string):
        self.data = input_string

    def linear_search(self, target):
        for i, char in enumerate(self.data):
            if char == target:
                return i
        return -1

    def process_data(self):
        if self.data.startswith("s") and self.data[1] != "b":
            index = self.linear_search("x")
            if index != -1:
                self.data += str(index)
        else:
            reversed_data = self.data[::-1]
            if reversed_data.startswith("s") and reversed_data[1] != "b":
                index = self.linear_search("x")
                if index != -1:
                    self.data = reversed_data + str(index)
            else:
                self.data = None

    def print_output(self):
        if self.data is not None:
            i = 0
            while i < len(self.data) - 2:
                if self.data[i] == self.data[i + 1] == self.data[i + 2]:
                    self.data = self.data[:i] + "(0_0)" + self.data[i + 3:]
                else:
                    i += 1
            print(self.data)


input_str = input()

if input_str.startswith("m"):
    mr_crab_obj = MrCrab(input_str)
    mr_crab_obj.process_data()
    mr_crab_obj.print_output()
elif input_str.startswith("sb"):
    spongebob_obj = SpongeBob(input_str)
    spongebob_obj.process_data()
    spongebob_obj.print_output()
elif input_str.startswith("s") and input_str[1] != "b":
    octopus_obj = Octopus(input_str)
    octopus_obj.process_data()
    octopus_obj.print_output()
else:
    reversed_str = input_str[::-1]
    if reversed_str.startswith("m"):
        mr_crab_obj = MrCrab(reversed_str)
        mr_crab_obj.process_data()
        mr_crab_obj.print_output()
    elif reversed_str.startswith("sb"):
        spongebob_obj = SpongeBob(reversed_str)
        spongebob_obj.process_data()
        spongebob_obj.print_output()
    elif reversed_str.startswith("s") and reversed_str[1] != "b":
        octopus_obj = Octopus(reversed_str)
        octopus_obj.process_data()
        octopus_obj.print_output()
    else:
        print("invalid input")

