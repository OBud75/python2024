from app import app

from app.models import Asset

@app.route("/<string:name>", methods=["GET"])
def asset_detail(name):
    return f"""
        <p>Asset: {Asset.get_by_name(name)}!</p>
    """
