

const FormatCurrency = (value) => {
    return new Intl.NumberFormat(process.env.REACT_APP_CURRENCY_LOCALE, {
         style: 'currency', currency: process.env.REACT_APP_CURRENCY,
         minimumFractionDigits:2, 
         maximumFractionDigits:2 
        }).format(value);
}

export default FormatCurrency;