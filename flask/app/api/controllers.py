# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, jsonify
from werkzeug import check_password_hash, generate_password_hash
from app import db
from app.api.models import Member

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/', methods=['GET'])
def index():
    return "MailBoard API Documentation. Current version: 1"


@api.route('/v1', methods=['GET'])
def v1():
    return "API v1.0"


@api.route('/v1/member/', methods=['GET', 'POST', 'DELETE', 'PUT', 'PATCH'])
def member():
    if request.method == 'GET':
        print(request.args)
        if not request.args:
            member_list = Member.query.all()
            return jsonify(member_list)
        elif request.args.get('Email'):
            return jsonify(Member.query.filter_by(email=request.args.get('Email')).first_or_404())
        elif request.args.get('Name'):
            return jsonify(Member.query.filter_by(name=request.args.get('Name')).all())
        else:
            return jsonify(('status', 404))
