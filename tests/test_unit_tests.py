import pytest
from App.models import Customer, Deceased, Grave, Graveyard, NavigationItem, Payment, Reservation, User, VirtualScene, MetaItem, Package
from App.models.customPackage import customPackage
from App.database import db
from datetime import datetime

@pytest.fixture
def customer():
    return Customer(name="John Doe", phone_number="1234567890", email_address="john@example.com")

def test_customer_initialization(customer):
    assert customer.get_name() == "John Doe"
    assert customer.get_phone_number() == "1234567890"
    assert customer.get_email_address() == "john@example.com"

@pytest.fixture
def deceased():
    return Deceased(name="Jane Doe", date_of_birth=datetime(1980, 1, 1), date_of_death=datetime(2020, 1, 1), cause_of_death="Natural Causes", grave_id="1")

def test_deceased_initialization(deceased):
    assert deceased.get_name() == "Jane Doe"
    assert deceased.get_cause_of_death() == "Natural Causes"

@pytest.fixture
def grave():
    return Grave(plot_num=1, graveyard_id="1", grave_type="single")

def test_grave_initialization(grave):
    assert grave.get_plot_num() == 1
    assert grave.get_grave_type() == "single"

@pytest.fixture
def graveyard():
    return Graveyard(name="Greenwood", location="City Center", max_plots=100, owner_id="1", single_price=1000.0, companion_price=1500.0, family_price=2000.0)

def test_graveyard_initialization(graveyard):
    assert graveyard.get_name() == "Greenwood"
    assert graveyard.get_location() == "City Center"

@pytest.fixture
def navigation_item():
    return NavigationItem(position={"x": 0, "y": 0}, source_scene_id=1, target_scene_id=2)

def test_navigation_item_initialization(navigation_item):
    assert navigation_item.source_scene_id == 1
    assert navigation_item.target_scene_id == 2

@pytest.fixture
def payment():
    return Payment(customer_id="1", user_id="1", amount=100.0, date_created=datetime.now())

def test_payment_initialization(payment):
    assert payment.get_amount() == 100.0

@pytest.fixture
def reservation():
    return Reservation(customer_id="1", reservation_date=datetime.now(), grave_id="1")

def test_reservation_initialization(reservation):
    assert reservation.get_customer_id() == "1"

@pytest.fixture
def user():
    return User(username="johndoe", password="password", role=3)

def test_user_initialization(user):
    assert user.username == "johndoe"
    assert user.role == 3

@pytest.fixture
def virtualscene():
    return VirtualScene(panorama_url="http://testurl.com/panorama")

def test_virtualscene_initialization(virtualscene):
    assert virtualscene.panorama_url == "http://testurl.com/panorama"

def test_virtualscene_get_json(virtualscene):
    assert virtualscene.get_json() == {
        "id": None,
        "panorama_url": "http://example.com/panorama",
        "arrows": [],
        "highlights": []
    }

def test_virtualscene_relationships(virtualscene):
    nav_item = NavigationItem(position={"x": 0, "y": 0}, source_scene_id=1, target_scene_id=2)
    virtualscene.outgoing_navigation.append(nav_item)
    assert len(virtualscene.outgoing_navigation) == 1

@pytest.fixture
def meta_item():
    return MetaItem(position={"x": 0, "y": 0}, virtualscene_id=1)

def test_meta_item_initialization(meta_item):
    assert meta_item.virtualscene_id == 1

@pytest.fixture
def package():
    return Package(name="Basic Package", description="A basic package", price=1000.0)

def test_package_initialization(package):
    assert package.name == "Basic Package"
    assert package.price == 1000.0

@pytest.fixture
def custom_package():
    return customPackage(base_price=500.0)

def test_custom_package_initialization(custom_package):
    assert custom_package.base_price == 500.0