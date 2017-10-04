#!/usr/bin/env python2

"""
   Obtains a Panda dataframe from a bouy using buoyant, with the following
   columns from waves as time-series:
           bandwidths
           center_frequencies
           mean_wave_direction
           polar_coordinate_r1
           polar_coordinate_r2
           principal_wave_direction
           spectral_energy
   It dumps this matrix and creates a PNG with these time-series (after
   normalizing them all).
"""

from buoyant import Buoy
import traceback
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def bouy_2_panda_df(buoy_id):
    """
       From a buoy_id, returns a Panda dataframe with the following columns
       as time-series:
           bandwidths
           center_frequencies
           mean_wave_direction
           polar_coordinate_r1
           polar_coordinate_r2
           principal_wave_direction
           spectral_energy
    """
    max_size = -1

    try:
        buoy_station = Buoy(buoy_id)

        y_bandwidths = []
        if 'bandwidths' in buoy_station.waves:
            y_bandwidths = buoy_station.waves['bandwidths']
        max_size = len(y_bandwidths)

        y_center_frequencies = []
        if 'center_frequencies' in buoy_station.waves:
            gen = (o.value for o in buoy_station.waves['center_frequencies'])
            y_center_frequencies = list(gen)
        max_size = max(max_size, len(y_center_frequencies))

        y_mean_wave_direction = []
        if 'mean_wave_direction' in buoy_station.waves:
            gen = (o.value for o in buoy_station.waves['mean_wave_direction'])
            y_mean_wave_direction = list(gen)
        max_size = max(max_size, len(y_mean_wave_direction))

        y_polar_coordinate_r1 = []
        if 'polar_coordinate_r1' in buoy_station.waves:
            gen = (o.value for o in buoy_station.waves['polar_coordinate_r1'])
            y_polar_coordinate_r1 = list(gen)
        max_size = max(max_size, len(y_polar_coordinate_r1))

        y_polar_coordinate_r2 = []
        if 'polar_coordinate_r2' in buoy_station.waves:
            gen = (o.value for o in buoy_station.waves['polar_coordinate_r2'])
            y_polar_coordinate_r2 = list(gen)
        max_size = max(max_size, len(y_polar_coordinate_r2))

        y_principal_wave_direction = []
        if 'principal_wave_direction' in buoy_station.waves:
            gen = (o.value for o in
                   buoy_station.waves['principal_wave_direction'])
            y_principal_wave_direction = list(gen)
        max_size = max(max_size, len(y_principal_wave_direction))

        y_spectral_energy = []
        if 'spectral_energy' in buoy_station.waves:
            gen = (o.value for o in buoy_station.waves['spectral_energy'])
            y_spectral_energy = list(gen)
        max_size = max(max_size, len(y_spectral_energy))

    except AttributeError as dummy_exc:
        traceback.print_exc()
        return None

    ts_df = pd.DataFrame(data=pad_list_2_np_array(y_bandwidths, max_size),
                         columns=['bandwidths'])

    ts_df['center_frequencies'] = (
        pad_list_2_np_array(y_center_frequencies, max_size))

    ts_df['mean_wave_direction'] = (
        pad_list_2_np_array(y_mean_wave_direction, max_size))

    ts_df['polar_coordinate_r1'] = (
        pad_list_2_np_array(y_polar_coordinate_r1, max_size))

    ts_df['polar_coordinate_r2'] = (
        pad_list_2_np_array(y_polar_coordinate_r2, max_size))

    ts_df['principal_wave_direction'] = (
        pad_list_2_np_array(y_principal_wave_direction, max_size))

    ts_df['spectral_energy'] = (
        pad_list_2_np_array(y_spectral_energy, max_size))

    return ts_df


def pad_list_2_np_array(num_list, expected_sz):
    """
       Convert a Python numeric list to a NumPy array with an expected
       dimension size.
       Returns such NumPy array.
    """
    np_arr = np.array([0.0] * (expected_sz - len(num_list)) + num_list)
    return np_arr.astype(np.float)


def main_test():
    """
       A main test. In this case, it just finds the dataframe for a buoy,
       and dumpts the dataframe to standard-output and saves its plot
       graph to a PNG file.
    """
    buoy_id = 41046
    ts_df = bouy_2_panda_df(buoy_id)

    with pd.option_context('display.max_rows', None,
                           'display.max_columns', None):
        print ts_df

    normalized_ts = (
        (ts_df - ts_df.values.min()) /
        (ts_df.values.max() - ts_df.values.min())
    )
    legend = (
        normalized_ts.plot()
        .legend(loc='center left', bbox_to_anchor=(1, 0.5))
    )

    plt.title('Buoy {}'.format(buoy_id), color='blue')
    fig = plt.gcf()
    fig.set_size_inches(9, 7)
    fig.savefig("plot_of_buoy_waves_ts.png", dpi=96,
                bbox_extra_artists=(legend,), bbox_inches='tight')

    # plt.show()


if __name__ == '__main__':
    main_test()
