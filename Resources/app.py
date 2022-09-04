
# importing pandas as pd
import pandas as pd
from IPython.display import HTML
  
# creating the dataframe
df = pd.read_csv('cities.csv')
  
html = df.to_html()
  
# write html to file
text_file = open("csvdata.html", "w")
text_file.write(html)
text_file.close()