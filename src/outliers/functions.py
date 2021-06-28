import numpy as np

def outliers_from_serie(serie):
    """

    Find outliers on a serie based in entire series quantiles.
        
    Parameters
    ----------

    :serie: array_like
            Input array or object that can be converted to an array.

    Returns
    -------

    :otlrs: array
    
    """
    
    ## Get quantiles
    Q1, Q3 = serie.quantile([0.25,0.75])

    ## Now, calculating the IQR, that is the difference between Q3 and Q1
    IQR = Q3 - Q1

    LO = Q1 - 1.5 * IQR
    HO = Q3 + 1.5 * IQR

    ## Filter outliers
    return (serie < LO) | (serie > HO)

   


def outliers_z_score(serie, window, treshold):
    """

    Find outliers on a serie based on z-scores.
        
    Parameters
    ----------

    :serie: array_like
            Input array or object that can be converted to an array.

    :windows: int

    :treshold: number of standard deviations to filter

    Returns
    -------

    :otlrs: array
    
    """

    u = serie.rolling(window, min_periods=1).mean()
    a = serie.rolling(window, min_periods=1).std()
    z = (serie - u)/a

    otlrs = (abs(z)>treshold)

    return otlrs

'''def find_outliers(serie, window):
    outliers = list()

    Q1 = serie.rolling(window, min_periods=1).quantile(.005, interpolation='lower')
    Q3 = serie.rolling(window, min_periods=1).quantile(.995, interpolation='lower')

    ##IQR = Q3 - Q1
    ##LO = Q1 - 1.5 * IQR
    ##HO = Q3 + 1.5 * IQR
    LO = Q1
    HO = Q3
    otlrs = ((serie > HO) | (serie < LO))

    return otlrs'''


def find_outliers(serie, cutoff_margin):
    """

    Find outliers on a serie based on percentiles.
        
    Parameters
    ----------

    :serie: array_like
            Input array or object that can be converted to an array.

    :cutoff_margin: represents the edges to be cut


    Returns
    -------

    :otlrs: array of booleans
    
    """
    #otlrs = abs(serie - serie.mean()) > serie.quantile(0.99999) - serie.mean()
    otlrs = (serie > serie.quantile(1 - cutoff_margin)) | (serie < serie.quantile(cutoff_margin))
    
    return otlrs


def drop_outliers(serie, fltr):
    serie.loc[fltr] = np.NaN