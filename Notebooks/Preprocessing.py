import pandas as pd


class FlightPreprocessor:

    def __init__(self, path):
        self.path = path
        self.df = None

    def load(self):
        self.df = pd.read_csv(self.path)
        return self

    def drop_columns(self):
        cols_to_drop = ['Unnamed: 0', 'flight']
        cols_to_drop = [c for c in cols_to_drop if c in self.df.columns]
        self.df = self.df.drop(cols_to_drop, axis=1)
        return self

    def fix_duration(self):

        def convert_duration(X):
            x = str(X)
            if '.' in x:
                h, m = x.split('.')
            else:
                h, m = x, '00'
            return f'{int(h):02d}:{int(m):02d}'

        self.df['duration'] = self.df['duration'].apply(convert_duration)
        return self

    def get_dataframe(self):
        return self.df
    
    def fit_transform(self):
        return self.load().drop_columns().fix_duration().get_dataframe()