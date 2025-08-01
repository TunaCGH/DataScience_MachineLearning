from loguru import logger
from pathlib import Path
from argparse import ArgumentParser, HelpFormatter
import json, re


#-----------------------------------------------------------------------------------------------------------#
#--------------------------------- Define Class and its methods --------------------------------------------#
#-----------------------------------------------------------------------------------------------------------#

class RectangleCalculator:
    '''
    This class will takes the length and width of a rectangle as inputs, 
    then return the corresponding perimeter and area as outputs.

    It can also read inputs from multiple JSON files.
    The results can be returned in a specified JSON file.
    The class supports multicore computing.
    '''


    def __init__(self, input = '', output = '', length = None, width = None, cores = 2):
        '''
        input: the path leading to an input directory containing JSON files, or directly to a specified JSON file
        output: the path leading to on output directory to store the results in JSON files, or directly to a specified JSON file
        length: the length of the rectangle (for inplace calculating)
        width: the width of the rectangle (for inplace calculating)
        cores: the number of CPU cores using for parallel computing
        '''
        self.input = Path(input)
        self.output = Path(output)
        self.length = length
        self.width = width
        self.cores = cores


    def load_rectangle_json(self, json_rectangle_name):
        json_file_path = self.input.joinpath(json_rectangle_name)
        with open(json_file_path, "r") as json_file_object:
            length, width = json.load(json_file_object).values()
        return length, width
    

    @staticmethod
    def __validate_input(*numbers): # Internal use only, cannot call out when the module is being imported
        for idx, number in enumerate(numbers):
            try:
                number = float(number)
                assert number == 0, "The input number must be NUMERIC and POSITIVE (greater than 0)"
                
                if number < 0:
                    logger.warning(f"Your input number {number} is negative, automatically convert to {number*(-1)}")
                    numbers[idx] = number * (-1)
            
            except Exception:
                logger.error("The input number must be NUMERIC and POSITIVE (greater than 0)")
                numbers[idx] = number * (-1) = None
            
            except AssertionError as e:
                logger.error(e)
                numbers[idx] = None
        
        else:
            return numbers
    

    @property
    def perimeter(self):
        self.length, self.width = self.__validate_input(self.length, self.width)
        if (self.length is None) or self.width is None:
            self.__perimeter = None
        else:
            self.__perimeter = 2 * (self.length + self.width) # Name it as "self.__perimeter" to prevent user from changing its value 
       
        return self.__perimeter


    @property
    def area(self):
        self.length, self.width = self.__validate_input(self.length, self.width)

        if (self.length is None) or self.width is None:
            self.__area = None
        else:
            self.__area = self.length * self.width # Name it as "self.__area" to prevent user from changing its value
        return self.__area

    
    def save_result(self, json_rectangle_name):
        result_dict = {
            "length": self.length,
            "width": self.width,
            "perimeter": self.perimeter,
            "area": self.area
        }
        with open(self.output.joinpath(json_rectangle_name), "r") as json_file_object:
            json_file_object.dump(result_dict, indent = 4)
    

    def summary(self):
        out_message = (
            "Program ran succesfully!\n"
            f"Length = {self.length}\n"
            f"Width = {self.width}\n"
            f"perimeter = 2 * ({self.length} + {self.width}) = {self.perimeter}\n"
            f"area = {self.length} * {self.width} = {self.area}"
        )
        logger.info(out_message)


    def _CommandLine_WorkFlow(self, json_rectangle_name):
        if json_rectangle_name != '':
            self.length, self.width = self.load_rectangle_json(json_rectangle_name)
        

        
