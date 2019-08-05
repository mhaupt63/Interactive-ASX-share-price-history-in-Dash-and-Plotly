# Interactive-ASX-share-price-history-in-Dash-and-Plotly
This is a project I did for the Udemy course "Interactive Python Dashboards with Plotly and Dash".  Hosted on herokun 
Check it out here https://mhaupt-asx.herokuapp.com/.  Username = 'JamesBond', password ='007'

There are 5 modules:
1. index.py.   This is the main module that calls the others
2. app.py.   This calls the external Dash stylesheets.  We use the BOOTSTRAP theme for the overall row&column layout
3. layouts.py.   This gives the layout of the dashboard
4. ASXcodes.py  This reads the ASX codes from the API module pyasx.  It also reads EFT codes from a spreadsheet Oz-etfs.csv, 
  which is manually updated from the website asxetfs.com
5. callbacks.py   This contains the callbacks that drive user interaction.  Price data is read from the API module alpha.vantage

There is also a spreadsheet with ETF codes Oz-etfs.csv,

