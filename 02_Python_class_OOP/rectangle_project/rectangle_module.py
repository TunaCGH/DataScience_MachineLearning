from loguru import logger
from pathlib import Path
from argparse import ArgumentParser, HelpFormatter
import json, re
from termcolor import colored
import multiprocessing

# Add file sink while keeping the default console output
logger_path = Path("02_Python_class_OOP/rectangle_project/rectangle_logs.txt")
if logger_path.exists():
    logger_path.unlink()

logger.add("02_Python_class_OOP/rectangle_project/rectangle_logs.txt", 
           rotation="1 MB",  # Rotate when file reaches 1MB
           retention="10 days",  # Keep logs for 10 days
           level="WARNING") # Only save the WARNING level and above

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
        self.input = input
        self.output = output
        self.__length = length
        self.__width = width
        self.cores = cores

        match str(self.output):
            case "":
                pass
            case _:
                self.output = Path(self.output)
                if (self.output.suffix != ""):
                    self.output = Path(self.output.parent, self.output.stem).mkdir(exist_ok = True)
                    logger.warning(f"Your output path should be a directory, not a file, automatically set as {self.output}")
                else:
                    self.output.mkdir(exist_ok = True)

    
    @staticmethod
    def __validate_input(*numbers): # Internal use only, cannot call out when the module is being imported
        numeric_pattern = r"^\d+\.?\d*$"
        numbers = list(numbers)
        for idx, number in enumerate(numbers):
            if re.match(numeric_pattern, str(number)):
                numbers[idx] = float(number)
            else:
                numbers[idx] = None
        
        return numbers


    def load_rectangle_json(self, json_rectangle_name):
        if len(Path(json_rectangle_name).parts) > 1:
            json_file_path = json_rectangle_name
        else:
            json_file_path = self.input.joinpath(json_rectangle_name)
        
        with open(json_file_path, "r") as json_pointer:
            length, width = json.load(json_pointer).values()
            length, width = RectangleCalculator.__validate_input(length, width)
        
        if None in [length, width]:
            logger.warning(f"The inputs in this {json_rectangle_name} file are corrupted!!!")
        return length, width
    

    @property
    def perimeter(self):
        self.length, self.width = self.__validate_input(self.length, self.width)
        if (self.length is None) or (self.width is None):
            self.__perimeter = None
        else:
            self.__perimeter = 2 * (self.length + self.width) # Name it as "self.__perimeter" to prevent user from changing its value 
       
        return self.__perimeter


    @property
    def area(self):
        self.length, self.width = self.__validate_input(self.length, self.width)

        if (self.length is None) or (self.width is None):
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
        
        json_rectangle_name = Path(json_rectangle_name).name
        if not json_rectangle_name.endswith(".json"):
            json_rectangle_name += ".json"
            logger.warning(f"The file does not end with '.json', automatically set as {json_rectangle_name}")
        with open(self.output.joinpath(json_rectangle_name), "w") as json_pointer:
            json.dump(result_dict, json_pointer, indent = 4)
    

    def summary(self, json_rectangle_name = "nameless"):
        match str(self.output):
            case "":
                json_rectangle_name = colored(json_rectangle_name, "red", attrs = ["bold"])
                out_message = (
                    f"Result of {json_rectangle_name} rectangle:\n"
                    f"++ Length = {self.length}\n"
                    f"++ Width = {self.width}\n"
                    f"++ Perimeter = 2 * ({self.length} + {self.width}) = {self.perimeter}\n"
                    f"++ Area = {self.length} * {self.width} = {self.area}"
                )
                logger.info(out_message)
            case _:
                self.save_result(json_rectangle_name)


    def _SingleInput_WorkFlow(self, json_rectangle_name):
        if json_rectangle_name != '':
            self.length, self.width = self.load_rectangle_json(json_rectangle_name)
            
            if (None not in [self.__length, self.__width]):
                logger.warning(f"Detected valid inputs in {json_rectangle_name}, prioritize them for calculation.")
  
            self.summary(json_rectangle_name)
        
        elif None in [self.__length, self.__width]:
            logger.error("No input was given")
        else:
            self.length, self.width = self.__length, self.__width
            self.summary()
            

#------------------------------------------------------------------------------------------------------------#
#------------------------------------------ Define main() function ------------------------------------------#
#------------------------------------------------------------------------------------------------------------#

def main():
    try:
        calculator = RectangleCalculator(
            input = "02_Python_class_OOP/rectangle_project/data/",
            output = "02_Python_class_OOP/rectangle_project/result",
            length = 2,
            width = 3,
            cores = 4
        )

        if calculator.input != "":
            calculator.input = Path(calculator.input)

            if calculator.input.suffix == ".json":
                calculator._SingleInput_WorkFlow(calculator.input)
            
            elif calculator.input.is_dir():
                input_files = [(entry.name,) for entry in calculator.input.glob("*.json") ]

                with multiprocessing.Pool(processes = calculator.cores) as pool:
                    pool.starmap(func = calculator._SingleInput_WorkFlow, iterable = input_files)

        else:
            calculator._SingleInput_WorkFlow('')
    
    except Exception as e:
        logger.error(e)


#---------------------------------------------------------------------------------------------------------#
#------------------------------------------ Run main() function ------------------------------------------#
#---------------------------------------------------------------------------------------------------------#

if __name__ == "__main__":
    main()