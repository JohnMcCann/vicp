

import tabula
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cc = plt.rcParams["axes.prop_cycle"].by_key()["color"]


class vicp:
    _vicp_report = ('https://www.hrsa.gov/sites/default/files/hrsa'
                    '/vaccine-compensation/data/data-statistics-report.pdf')
    
    def __init__(self, report='data-statistics-report.pdf',
                 template='tabula-template.json'):
        try:
            self.dfs = tabula.read_pdf_with_template(
                report, template, pandas_options={'header':None}
            )
        except:
            with open(report, 'wb') as f:
                f.write(requests.get(self._vicp_report).content)
            self.dfs = tabula.read_pdf_with_template(
                report, template, pandas_options={'header':None}
            )
        self.form_tables()
        return


    def form_tables(self):
        # VICP Adjudication Categories, by Alleged Vaccine for Petitions Filed
        # Since the Inclusion of Influenza as an Eligible Vaccine for Filings
        # 01/01/2006 through 12/31/2018
        temp = pd.concat([self.dfs[0], self.dfs[1]], ignore_index=True)
        temp.drop(temp.index[-1], inplace=True)
        temp.iloc[:,1:] = (
            temp.iloc[:,1:].replace('[,]', '', regex=True).astype(int)
        )
        temp.columns = ['Vaccine', 'Doses', 'Concessions', 'Verdicts',
                        'Settlements', 'Compensations', 'Dismissed', 'Totals']
        self.adjudications = temp
        # Petitions Filed, Compensated and Dismissed, by
        # Alleged Vaccine, Since the Beginning of VICP,
        # 10/01/1988 through 09/01/2020
        temp = self.dfs[2].copy()
        temp.drop(temp.index[-1], inplace=True)
        temp.iloc[:,1:] = (
            temp.iloc[:,1:].replace('[,]', '', regex=True).astype(int)
        )
        temp.columns = ['Vaccine', 'Injury', 'Death', 'Totals', 'Compensated',
                        'Dismissed']
        self.petitions = temp
        # Petitions Filed
        temp = self.dfs[3].copy()
        temp = temp.rename(columns=temp.iloc[0]).drop(temp.index[0])
        temp.drop(temp.index[-1], inplace=True)
        temp.iloc[:,0] = temp.iloc[:,0].replace('[FY ]', '', regex=True)
        temp.iloc[:,1] = temp.iloc[:,1].replace('[,]', '', regex=True).astype(int)
        temp['Fiscal Year'] = pd.to_datetime(temp['Fiscal Year'], format='%Y')
        self.annual_petitions = temp
        # Adjudications
        temp = self.dfs[4].copy()
        temp = temp.rename(columns=temp.iloc[0]).drop(temp.index[0])
        temp.drop(temp.index[-1], inplace=True)
        temp.iloc[:,1:] = (
            temp.iloc[:,1:].replace('[,]', '', regex=True).astype(int)
        )
        temp.iloc[:,0] = temp.iloc[:,0].replace('[FY ]', '', regex=True)
        temp['Fiscal Year'] = pd.to_datetime(temp['Fiscal Year'], format='%Y')
        self.annual_adjudications = temp
        # Awards Paid
        temp = pd.concat([self.dfs[5], self.dfs[6]], ignore_index=True)
        temp.columns = ['Year', 'Awards', 'Amount', 'Attorney Fees',
                          'Attorney Payments (Dismissed)', 'Attorney Fees (Dismissed)',
                          'Interim Payments', 'Interim Fees', 'Totals']
        temp.drop(temp.index[-1], inplace=True)
        currency_columns = [2,3,5,7,8]
        for col in currency_columns:
            temp.iloc[:,col] = temp.iloc[:,col].replace('[\$,)]', '',
                                                            regex=True).astype(float)
        integer_columns = [1, 4, 6]
        for col in integer_columns:
            temp.iloc[:,col] = temp.iloc[:,col].replace('[,]', '', regex=True).astype(int)
        temp.iloc[:,0] = temp.iloc[:,0].replace('[FY ]', '', regex=True)
        temp['Year'] = pd.to_datetime(temp['Year'], format='%Y')
        self.awards = temp