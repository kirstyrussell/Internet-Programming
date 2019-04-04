#  Kirsty Russell
#  CS 4720
#  Assignment 2
#  Professor Setzer
#  January 31, 2019

import sqlite3


def get_all_areas() -> object:
    """Returns a list of tuples representing all the rows in the area table."""

    conn = sqlite3.connect("measures.sqlite")
    crs = conn.cursor()
    crs.execute("select * from area")
    results = []

    for row in crs.fetchall():
        results.append(row)

    return results


def get_locations_for_area(area_id):
    """Return a list of tuples giving the locations for the given area."""

    conn = sqlite3.connect("measures.sqlite")

    crs = conn.cursor()

    crs.execute("select * from location where location_area = " + str(area_id))
    results = []

    for row in crs.fetchall():
        results.append(row)

    return results

    conn.close()


def get_measurements_for_location(location_id):
    """Return a list of tuples giving the measurement rows for the given location."""

    conn = sqlite3.connect("measures.sqlite")

    crs = conn.cursor()

    crs.execute("select * from measurement where measurement_location = " + str(location_id))
    results = []

    for row in crs.fetchall():
        results.append(row)

    return results

    conn.close()


def get_categories_for_area(area_id):

    """Return a list of rows from the category table that all contain the given area."""

    conn = sqlite3.connect("measures.sqlite")

    crs = conn.cursor()

    crs.execute("select * from category where category_id in (select category_id from category_area" \
              " where area_id = " + str(area_id) + ")")
    results = []

    for row in crs.fetchall():
        results.append(row)

    return results

    conn.close()
