# Flight-Management-System
// Flight Search Service
function searchFlight(departure, arrival, date) {
    if (departure is empty or arrival is empty) {
        return "Please enter valid search criteria.";
    }

    flights = findFlights(departure, arrival, date);
    if (flights is empty) {
        return "No flights available for the specified criteria.";
    } else {
        return flights;
    }
}

// Flight Booking Service
function bookFlight(flight, passengerDetails, paymentDetails) {
    if (passengerDetails is incomplete) {
        return "Please complete all required fields.";
    }

    if (paymentDetails is invalid) {
        return "Payment failed. Please check your payment details.";
    }

    bookingReference = confirmBooking(flight, passengerDetails, paymentDetails);
    return "Booking confirmed. Reference number: " + bookingReference;
}

// Flight Schedule Service
function viewSchedule(flightNumber) {
    schedule = getSchedule(flightNumber);
    if (schedule is empty) {
        return "Invalid flight number.";
    } else {
        return schedule;
    }
}

// Flight Cancel Service
function cancelFlight(bookingReference) {
    if (bookingReference is invalid) {
        return "Invalid booking reference.";
    }

    cancellationAllowed = checkCancellationTime(bookingReference);
    if (!cancellationAllowed) {
        return "Cannot cancel the flight as it is too close to the departure time.";
    }

    cancellationReference = confirmCancellation(bookingReference);
    return "Flight canceled. Cancellation reference number: " + cancellationReference; }
