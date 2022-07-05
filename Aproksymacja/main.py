# import required module
from Data import *
from LangrangeInterpolation import *
from SplinesInterpolation import *

# assign directory
directory = 'data'

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data_dir = Data(directory)
    data, filenames = data_dir.get_data()

    langrange = Langrange(data, filenames)
    langrange.langrangeInterpolation()

    print("-------------")

    splines = Splines(data, filenames)
    splines.splinesInterpolation()

