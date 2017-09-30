# WIP

This project is a *work in progress*. The implementation is *incomplete* and subject to change. The documentation can be inaccurate.

# Requeriments

The required modules may be installed (probably under a virtualenv) using:

      pip install -r requirements.txt

Note: before installing `matplotlib`, it may be necessary that your system has installed the packages with the C header files and .SO files for `libpng-devel` and `freetype-devel`.

# Info

Get the waves time-series of a National Buoy Data Center buoy into a Panda dataframe, using buoyant.

This example also creates a PNG file with the plot of those time-series (after normalization, so all the time-series may be combined into a single plot).

<p align="center">
<img src="https://raw.githubusercontent.com/je-nunez/buoy_2_panda/master/plot_of_buoy_waves_ts.png" height="500px">
</p>

