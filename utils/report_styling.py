import pandas as pd
import os

class DataFrameStyler:
    def __init__(self,data_frame):
        self.df = data_frame
        self.styled_df = None

    @staticmethod
    def highlight_header():
        return [ {'selector': 'thead th',
            'props': 'background-color: #002366; color: white; font-weight: bold;' }]

    @staticmethod
    def add_cell_borders():
        return {
            'selector': 'td, th',
            'props': 'border: 1px solid black;'
        }

    @staticmethod
    def highlight_cells(val):
        if val == 'Both Null':
            return 'background-color: #F9B5AC; color: black; font-weight: bold;'
        elif val == 'Not Matched':
            return 'background-color: #E31C25; color: white; font-weight: bold;'
        elif val == 'Items Not Found':
            return 'background-color: #EFDAF7; color: white; font-weight: bold;'
        elif val == 'Only in Prod':
            return 'background-color: #ADD8E6; color: black; font-weight: bold;'
        elif val == 'Only in Stage':
            return 'background-color: #ADD8E6; color: black; font-weight: bold;'
        elif val == 'Match':
            return 'background-color: #C9F2C7; color: black; font-weight: bold;'
        else:
            return None

    def apply_styling_comparison_report(self):
        def convert_to_url(cell):
            return f'<a href="{cell}" target="_blank">{cell}</a>' if cell else None

        self.df['URL'] = self.df['URL'].apply(convert_to_url)
        self.df['Staging URL'] = self.df['Staging URL'].apply(convert_to_url)
        self.styled_df = self.df.style.set_table_styles([self.add_cell_borders()]+self.highlight_header())\
                        .map(self.highlight_cells)\


    def apply_styling_data_report(self):
        def convert_to_url(cell):
            return f'<a href="{cell}" target="_blank">{cell}</a>' if cell else None

        self.df['URL'] = self.df['URL'].apply(convert_to_url)
        self.df['canonical link'] = self.df['canonical link'].apply(convert_to_url)
        self.df['og:url'] = self.df['og:url'].apply(convert_to_url)
        self.styled_df = self.df.style.set_table_styles([self.add_cell_borders()]+self.highlight_header())\

    def generate_style_report(self, file_path):
        if self.styled_df is None:
            raise ValueError("Styling has not been applied. Call apply_styling() before generating the report.")

        print('generate_style_report call start')
        table_name = os.path.basename(file_path).split('.')[0]
        table_name_row = pd.DataFrame([[table_name] + [''] * (len(self.df.columns) - 1)], columns=self.df.columns)
        table_name_row.index = ['']
        html_table_name = f"<h2 style='text-align: center;'>{table_name}</h2>"
        self.styled_df.hide(axis= 'index')
        styled_html = self.styled_df.to_html(index= False)
        html_report = f"{html_table_name}\n{styled_html}"

        with open(file_path, "w") as file:
            file.write(html_report)