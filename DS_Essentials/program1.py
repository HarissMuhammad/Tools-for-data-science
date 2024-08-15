# def safe_divide(x, y):
"""_summary_
   # Returns:
    _type_: _description_
# # # """
# # # #     try:
# # # #         z = x/y
# # # #         print(z)
# # # #     except ZeroDivisionError:
# # # #         print("Error: Cannot Divide By zero")
# # # #     except ValueError:
# # # #         print("You didn't provide a number")
# # # #         return None
# # # #     finally:
# # # #         print("Success")
# # # #     return None


# # # # a = int(input("Enter numerator"))
# # # # b = int(input("Enter denomintator"))
# # # # print(safe_divide(a, b))
# # # # Type your code here
# # # import math


# # # def perform_calculation(number1):
# # #     try:
# # #         result = math.sqrt(number1)
# # #         print(f"Result: {result}")
# # #     except ValueError:
# # #         print("Error: Invalid input! Please enter a positive integer or a float value.")


# # # # Test case
# # # number1 = float(input("Enter the number:-"))
# # # perform_calculation(number1)

# # list_num = [1,2,3,6,7,83,34]
# # list_num.append(45)
# # print(sorted(list_num))
# # printlist_num.sort()

# class circle:
#     def __init__(self,radius):
#         self.radius = radius


# class rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width

# c1 = circle(2)
# c1.radius(2)
class TextAnalyzer:
    """
    TextAnalyzer class is designed to process and analyze text.

    Attributes:
        text (str): The input text to be analyzed.
    """

    def __init__(self, text):
        formatted_text = text.replace(',', ' ').replace(
            '!', ' ').replace(".", " ").replace("?", " ")

        formatted_text = formatted_text.lower()

        self.fmt_txt = formatted_text

    def freq_all(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        word_list = self.fmt_txt.split(" ")

        dictc = {}

        for word in set(word_list):
            dictc[word] = word_list.count(word)

        return dictc

    def freq_of(self, word):
        """_summary_

        Args:
            word (_type_): _description_

        Returns:
            _type_: _description_
        """
        freq_dict = self.freq_all()

        if word in freq_dict:
            return freq_dict[word]


GIVENSTRING = "Lorem ipsum dolor! To be, it seems Lorem great. But no sad time. To work and? And great. And to love."

analyzed = TextAnalyzer(GIVENSTRING)

print("Formatted text: ",analyzed.fmt_txt)

freq_map = analyzed.freq_all()
print("Unique words are: ",freq_map)

word = "lorem"
specific = analyzed.freq_of(word)

print(f"The word {word} apears {specific} times")

