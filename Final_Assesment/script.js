document.addEventListener('DOMContentLoaded', () => {
    // Flight Search Service
    document.getElementById('searchForm').addEventListener('submit', (event) => {
        event.preventDefault();
        const departure = document.getElementById('departure').value;
        const arrival = document.getElementById('arrival').value;
        const date = document.getElementById('date').value;

        if (!departure || !arrival) {
            document.getElementById('searchResults').textContent = "Please enter valid search criteria.";
            return;
        }

        // Simulate API call
        const flights = findFlights(departure, arrival, date);
        document.getElementById('searchResults').textContent = flights.length ? flights.join(', ') : "No flights available for the specified criteria.";
    });

    // Flight Booking Service
    document.getElementById('bookingForm').addEventListener('submit', (event) => {
        event.preventDefault();
        const flight = document.getElementById('flight').value;
        const passengerDetails = {
            name: document.getElementById('name').value,
            age: document.getElementById('age').value,
            passport: document.getElementById('passport').value,
        };
        const paymentDetails = {
            card: document.getElementById('card').value,
            expiry: document.getElementById('expiry').value,
            cvv: document.getElementById('cvv').value,
        };

        if (!completePassengerDetails(passengerDetails)) {
            document.getElementById('bookingResult').textContent = "Please complete all required fields.";
            return;
        }

        if (!validatePayment(paymentDetails)) {
            document.getElementById('bookingResult').textContent = "Payment failed. Please check your payment details.";
            return;
        }

        const bookingReference = confirmBooking(flight, passengerDetails, paymentDetails);
        document.getElementById('bookingResult').textContent = `Booking confirmed. Reference number: ${bookingReference}`;
    });

    // Flight Schedule Service
    document.getElementById('scheduleForm').addEventListener('submit', (event) => {
        event.preventDefault();
        const flightNumber = document.getElementById('flightNumber').value;
        const schedule = getSchedule(flightNumber);

        document.getElementById('scheduleResult').textContent = schedule ? JSON.stringify(schedule) : "Invalid flight number.";
    });

    // Flight Cancel Service
    document.getElementById('cancelForm').addEventListener('submit', (event) => {
        event.preventDefault();
        const bookingReference = document.getElementById('bookingReference').value;

        if (!validateBookingReference(bookingReference)) {
            document.getElementById('cancelResult').textContent = "Invalid booking reference.";
            return;
        }

        if (!checkCancellationTime(bookingReference)) {
            document.getElementById('cancelResult').textContent = "Cannot cancel the flight as it is too close to the departure time.";
            return;
        }

        const cancellationReference = confirmCancellation(bookingReference);
        document.getElementById('cancelResult').textContent = `Flight canceled. Cancellation reference number: ${cancellationReference}`;
    });

    // Mock functions to simulate API behavior
    function findFlights(departure, arrival, date) {
        return ["Flight1", "Flight2"]; // Example return value
    }

    function completePassengerDetails(details) {
        return details.name && details.age && details.passport;
    }

    function validatePayment(details) {
        return details.card && details.expiry && details.cvv;
    }

    function confirmBooking(flight, passengerDetails, paymentDetails) {
        return "ABC123"; // Example booking reference
    }

    function getSchedule(flightNumber) {
        return flightNumber === "Flight1" ? { departure: "10:00 AM", arrival: "12:00 PM" } : null;
    }

    function validateBookingReference(reference) {
        return reference === "ABC123";
    }

    function checkCancellationTime(reference) {
        return true; // Assume cancellation is allowed for simplicity
    }

    function confirmCancellation(reference) {
        return "XYZ789"; // Example cancellation reference
    }
});
