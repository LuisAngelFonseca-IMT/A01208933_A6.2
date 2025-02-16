"""Hotel Reservation System Module.

This module implements the classes and methods for managing hotels, customers,
and reservations with persistent storage in JSON files.
"""

import json
import os
import unittest


class Hotel:
    """Class representing a hotel with basic information
    and room availability."""

    def __init__(self, hotel_id, name, location, rooms_available):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.rooms_available = rooms_available

    def to_dict(self):
        """Convert hotel object to dictionary."""
        return self.__dict__

    def __repr__(self):
        """String representation of the hotel."""
        return f"""Hotel({self.name},
        {self.location}, {self.rooms_available} rooms)"""


class Customer:
    """Class representing a customer with ID, name, and email."""

    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def to_dict(self):
        """Convert customer object to dictionary."""
        return self.__dict__

    def __repr__(self):
        """String representation of the customer."""
        return f"Customer({self.name}, {self.email})"


class Reservation:
    """Class representing a reservation linking a customer to a hotel."""
    def __init__(self, reservation_id, customer_id, hotel_id):
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id

    def to_dict(self):
        """Convert reservation object to dictionary."""
        return self.__dict__

    def __repr__(self):
        """String representation of the reservation."""
        return f"""Reservation(Customer ID: {self.customer_id},
        Hotel ID: {self.hotel_id})"""


class Persistence:
    """Utility class for loading and saving JSON data."""
    @staticmethod
    def load_data(file_name):
        """Load data from a JSON file."""
        if os.path.exists(file_name):
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print(f"Error reading {file_name}. Invalid format.")
                return []
        return []

    @staticmethod
    def save_data(file_name, data):
        """Save data to a JSON file."""
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)


class HotelManager:
    """Manager class for hotel-related operations."""

    FILE = 'hotels.json'

    @classmethod
    def create_hotel(cls, hotel):
        """Create a new hotel."""
        hotels = Persistence.load_data(cls.FILE)
        hotels.append(hotel.to_dict())
        Persistence.save_data(cls.FILE, hotels)

    @classmethod
    def delete_hotel(cls, hotel_id):
        """Delete a hotel by ID."""
        hotels = Persistence.load_data(cls.FILE)
        hotels = [h for h in hotels if h['hotel_id'] != hotel_id]
        Persistence.save_data(cls.FILE, hotels)

    @classmethod
    def display_hotel(cls, hotel_id):
        """Display hotel information by ID."""
        hotels = Persistence.load_data(cls.FILE)
        for hotel in hotels:
            if hotel['hotel_id'] == hotel_id:
                print(hotel)

    @classmethod
    def modify_hotel(cls, hotel_id, new_info):
        """Modify hotel information."""
        hotels = Persistence.load_data(cls.FILE)
        for hotel in hotels:
            if hotel['hotel_id'] == hotel_id:
                hotel.update(new_info)
        Persistence.save_data(cls.FILE, hotels)


class CustomerManager:
    """Manager class for customer-related operations."""

    FILE = 'customers.json'

    @classmethod
    def create_customer(cls, customer):
        """Create a new customer."""
        customers = Persistence.load_data(cls.FILE)
        customers.append(customer.to_dict())
        Persistence.save_data(cls.FILE, customers)

    @classmethod
    def delete_customer(cls, customer_id):
        """Delete a customer by ID."""
        customers = Persistence.load_data(cls.FILE)
        customers = [c for c in customers if c['customer_id'] != customer_id]
        Persistence.save_data(cls.FILE, customers)

    @classmethod
    def display_customer(cls, customer_id):
        """Display customer information by ID."""
        customers = Persistence.load_data(cls.FILE)
        for customer in customers:
            if customer['customer_id'] == customer_id:
                print(customer)

    @classmethod
    def modify_customer(cls, customer_id, new_info):
        """Modify customer information."""
        customers = Persistence.load_data(cls.FILE)
        for customer in customers:
            if customer['customer_id'] == customer_id:
                customer.update(new_info)
        Persistence.save_data(cls.FILE, customers)


class ReservationManager:
    """Manager class for reservation-related operations."""

    FILE = 'reservations.json'

    @classmethod
    def create_reservation(cls, reservation):
        """Create a new reservation."""
        reservations = Persistence.load_data(cls.FILE)
        reservations.append(reservation.to_dict())
        Persistence.save_data(cls.FILE, reservations)

    @classmethod
    def cancel_reservation(cls, reservation_id):
        """Cancel a reservation by ID."""
        reservations = Persistence.load_data(cls.FILE)
        reservations = [r for r in reservations if
                        r['reservation_id'] != reservation_id]
        Persistence.save_data(cls.FILE, reservations)


class TestHotelReservationSystem(unittest.TestCase):
    """Test cases for the hotel reservation system."""
    def setUp(self):
        """Set up initial test data."""
        self.hotel = Hotel('1', 'Grand Plaza', 'New York', 100)
        self.customer = Customer('1', 'John Doe', 'john@example.com')
        self.reservation = Reservation('1', '1', '1')

    def test_create_and_display_hotel(self):
        """Test creating and displaying a hotel."""
        HotelManager.create_hotel(self.hotel)
        hotels = Persistence.load_data('hotels.json')
        self.assertTrue(any(h['hotel_id'] == '1' for h in hotels))

    def test_create_and_display_customer(self):
        """Test creating and displaying a customer."""
        CustomerManager.create_customer(self.customer)
        customers = Persistence.load_data('customers.json')
        self.assertTrue(any(c['customer_id'] == '1' for c in customers))

    def test_create_and_cancel_reservation(self):
        """Test creating and canceling a reservation."""
        ReservationManager.create_reservation(self.reservation)
        reservations = Persistence.load_data('reservations.json')
        self.assertTrue(any(r['reservation_id'] == '1' for r in reservations))
        ReservationManager.cancel_reservation('1')
        reservations = Persistence.load_data('reservations.json')
        self.assertFalse(any(r['reservation_id'] == '1' for r in reservations))


if __name__ == '__main__':
    unittest.main()
