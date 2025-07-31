from src.product import Product


def test_product_init():
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    assert product.name == "Iphone 15"
    assert product.description == "512GB, Gray space"
    assert product.price == 210000.0
    assert product.quantity == 8