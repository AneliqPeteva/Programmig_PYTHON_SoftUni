from collections import deque
from unittest import TestCase, main

from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):
    def setUp(self):
        self.s = RailwayStation("Sofia")

    def test_initialised_correctly(self):
        s = RailwayStation("Sofia")
        self.assertEqual(s.name, "Sofia")
        self.assertEqual(s.arrival_trains, deque())
        self.assertEqual(s.departure_trains, deque())

    def test_less_name_chars_raises(self):
        with self.assertRaises(ValueError) as ex:
            s = RailwayStation("So")
        self.assertEqual(str(ex.exception), "Name should be more than 3 symbols!")

        with self.assertRaises(ValueError) as ex:
            s = RailwayStation("Sof")
        self.assertEqual(str(ex.exception), "Name should be more than 3 symbols!")

    def test_new_arrival_on_board(self):
        self.assertEqual(len(self.s.arrival_trains), 0)
        self.assertEqual(self.s.arrival_trains, deque())

        self.s.new_arrival_on_board("Some info")

        self.assertEqual(len(self.s.arrival_trains), 1)
        self.assertEqual(self.s.arrival_trains, deque(["Some info"]))

        self.s.new_arrival_on_board("Some info 2")
        self.assertEqual(len(self.s.arrival_trains), 2)
        self.assertEqual(self.s.arrival_trains, deque(["Some info", "Some info 2"]))

    def test_train_has_arrived_other_trains(self):
        self.s.new_arrival_on_board("Some info")

        self.assertEqual(len(self.s.arrival_trains), 1)
        self.assertEqual(len(self.s.departure_trains), 0)

        train_info = "Some info2"
        result = self.s.train_has_arrived(train_info)
        expected_message = f"There are other trains to arrive before {train_info}."
        self.assertEqual(result, expected_message)

        self.assertEqual(len(self.s.arrival_trains), 1)
        self.assertEqual(len(self.s.departure_trains), 0)

    def test_train_has_arrived_go_to_departure(self):
        self.s.new_arrival_on_board("Some info")

        self.assertEqual(len(self.s.arrival_trains), 1)
        self.assertEqual(len(self.s.departure_trains), 0)

        train_info = "Some info"
        result = self.s.train_has_arrived(train_info)
        expected_message = f"{train_info} is on the platform and will leave in 5 minutes."
        self.assertEqual(result, expected_message)

        self.assertEqual(len(self.s.arrival_trains), 0)
        self.assertEqual(len(self.s.departure_trains), 1)

    def test_train_has_left_no_departure_trains(self):
        self.s.new_arrival_on_board("Some info")

        self.assertEqual(len(self.s.arrival_trains), 1)
        self.assertEqual(len(self.s.departure_trains), 0)

        result = self.s.train_has_left("Some info")
        self.assertFalse(result)

    def test_train_has_left_same_info(self):
        self.s.new_arrival_on_board("Some info")
        self.s.train_has_arrived("Some info")

        self.assertEqual(len(self.s.departure_trains), 1)
        self.assertEqual(len(self.s.arrival_trains), 0)

        result = self.s.train_has_left("Some info")

        self.assertTrue(result)
        self.assertEqual(len(self.s.departure_trains), 0)
        self.assertEqual(len(self.s.arrival_trains), 0)

        self.assertEqual(self.s.departure_trains, deque())

    def test_train_has_left_different_info(self):
        self.s.new_arrival_on_board("Some info")
        self.s.train_has_arrived("Some info")

        self.assertEqual(len(self.s.departure_trains), 1)
        self.assertEqual(len(self.s.arrival_trains), 0)

        result = self.s.train_has_left("Different info")

        self.assertFalse(result)
        self.assertEqual(len(self.s.departure_trains), 1)
        self.assertEqual(len(self.s.arrival_trains), 0)


if __name__ == "__main__":
    main()