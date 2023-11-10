.. _use_cases:

=========
Use cases
=========

.. sidebar:: Contents

    .. contents::
        :local:
        :depth: 1


The widgets provided with qtbricks should work as any other Qt widget in Python. Hence, including them in your GUI should be pretty straight-forward. The more complex part of any GUI after having finished the (user-friendly) layout is to wire up and connect all the different widgets. Here the widgets provided with qtbricks focus at exposing a minimalistic public API and appropriate Qt signals and slots.


General usage
=============

Using a widget from qtbricks should normally be straight-forward:

* Import the qtbricks package.
* Create an instance of the widget of your choice.
* Add the widget to some layout of your GUI.

The less straight-forward and much more individual part is wiring the signals and slots and connecting the widget with the business logic of your application.

