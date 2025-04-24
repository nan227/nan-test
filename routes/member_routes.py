from flask import Blueprint, request, jsonify
from models.book import Book
from models.issued_book import IssuedBook

member_routes = Blueprint('member', __name__)

@member_routes.route('/member/login', methods=['POST'])
def member_login():
    # Handle member login logic
    pass

@member_routes.route('/member/search', methods=['GET'])
def search_books():
    # Handle book search logic
    pass

@member_routes.route('/member/issue', methods=['POST'])
def issue_book():
    # Handle book issue logic
    pass

@member_routes.route('/member/return', methods=['POST'])
def return_book():
    # Handle book return logic
    pass