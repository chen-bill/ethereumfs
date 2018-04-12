from flask import Flask, jsonify, request

app = Flask(__name__)

with open("pi.txt", "r") as f:
    PI = f.readline()


@app.route('/save/{hex_string}', methods=['POST'])
def save(hex_string):
    save_file(hex_string)
    return jsonify({'success', ''})


@app.route('/fetch', methods=['GET'])
def fetch():
    get_file(request.args.get('document_index'))
    return jsonify({'success', ''})


def get_file():
    # TOOD some web3 stuff
    pass


def save_file(hex_string):
    get_metadata(hex_string)
    # TODO some web3 stuff


def get_metadata(hex_string):
    return (PI.find(hex_string), len(hex_string))


def decode_metadata(ind, length):
    return (PI[ind:ind+length].decode("hex"))


if __name__ == '__main__':
    app.run(debug=True)
