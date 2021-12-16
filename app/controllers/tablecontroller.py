from app.controllers.controller import ControllerBase
from tests.fileReader import Read

from flask import render_template

class TableController(ControllerBase):
    @staticmethod
    def get():
        df = Read.DataFrameFromCSVFile()
        return render_template('table.html', titles=df.columns.values, row_data=list(df.values.tolist()), zip=zip)

