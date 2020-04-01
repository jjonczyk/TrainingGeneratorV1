import xlrd


class Database:
    def __init__(self):
        self.CARDIO = []
        self.ABS = []
        self.CORE = []
        self.CHEST = []
        self.BACK = []
        self.GLUTES = []
        self.LEGS = []
        self.ARMS = []
        self.WARMUP = []
        self.HIIT = []
        self.DATA = {
            "CARDIO": self.CARDIO,
            "ABS": self.ABS,
            "CORE": self.CORE,
            "CHEST": self.CHEST,
            "BACK": self.BACK,
            "GLUTES": self.GLUTES,
            "LEGS": self.LEGS,
            "ARMS": self.ARMS,
            "WARMUP": self.WARMUP,
            "HIIT": self.HIIT,
        }

    def import_data(self):
        workbook = xlrd.open_workbook("data.xlsx")
        worksheet = workbook.sheet_by_name("workout")
        number_of_rows = worksheet.nrows
        number_of_columns = worksheet.ncols
        table = list()
        record = list()

        for x in range(number_of_rows):
            for y in range(number_of_columns):
                record.append(worksheet.cell(x,y).value)
            table.append(record)
            record = []

        for i in range(number_of_rows):
            if (i > 0):
                muscle_parts = table[i][7]
                for key in self.DATA.keys():
                    if (key in muscle_parts):
                        self.DATA[key].append(table[i])
