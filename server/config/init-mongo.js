db = db.getSiblingDB('fgo-db');

db.createCollection('users');
db.createCollection('cards');
db.createCollection('invoices');
db.createCollection('transactions');
