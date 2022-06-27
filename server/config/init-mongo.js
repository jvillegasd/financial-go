db = db.getSiblingDB('database-financial-go');

db.createCollection('users');
db.createCollection('cards');
db.createCollection('invoices');
db.createCollection('transactions');
