import datetime
import hashlib
import json

from flask import Flask, jsonify


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(poof=1, previous_hash='0')

    def create_block(self, poof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'poof': poof,
            'previous_hash': previous_hash

        }
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def poof_of_world(self, previous_poof):
        new_poof = 1
        check_poof = False

        while check_poof is False:
            hash_operation = hashlib.sha256(str(new_poof ** 2 - previous_poof ** 2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_poof = True
            else:
                new_poof += 1
            return new_poof

    def hash_block(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain, new_poof=None):
        previous_block = chain[0]
        index_block = 1
        while index_block < len(chain):
            block = chain[index_block]
            if block['previous_hash'] != self.hash_block(previous_block):
                return False
            previous_poof = previous_block['poof']
            poof = block['poof']
            hash_operation = hashlib.sha256(str(new_poof ** 2 - previous_poof ** 2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False

            previous_block = block
            index_block += 1

        return True


app = Flask(__name__)
blockchain = Blockchain()


@app.route('/mine_block', methods=['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_poof = previous_block['poof']
    poof = blockchain.poof_of_world(previous_poof)
    previous_hash = blockchain.hash_block(previous_block)
    block = blockchain.create_block(poof, previous_hash)
    response = {
        'message': 'Felicidade, a conseguido mina un bloque ',
        'index': block['index'],
        'time': block['timestamp'],
        'poof': block['poof'],
        'previous_hash': block['previous_hash'],

    }
    return jsonify(response), 200


@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200


app.run(host="0.0.0.0", port=5000, debug=True)
