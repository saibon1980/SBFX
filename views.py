"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from SBFX import app
from flask import Flask
from flask import request
import json
import traceback


@app.route('/')
@app.route('/Wallet')
def Wallet():
    """Renders the wallet."""
    return render_template(
        'wallet.html',
        title='Wallet',
        year=datetime.now().year,
    )

@app.route('/Datasets')
def Datasets():
    """Renders the Datasets."""
    return render_template(
        'datasets.html',
        title='Datasets',
        year=datetime.now().year,
        message='Download SBFX datasets from server.'
    )

@app.route('/SBFXhub')
def SBFXhub():
    """Renders the hub."""
    return render_template(
        'hub.html',
        title='SBFXhub',
        year=datetime.now().year,
        message='Hub with general information on protocol and process.'
    )
