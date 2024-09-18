// TMSRestApi.java
// Rest API for the travel management system (TMS)

public class TMSRestApi {
    // Endpoint to get all available flights
    @GET("/flights")
    public List<Flight> getAllFlights() {
        // Implementation to fetch and return all available flights
        return flightService.getAllFlights();
    }

    // Endpoint to book a flight for a user
    @POST("/bookings")
    public Booking bookFlight(@RequestBody BookingRequest request) {
        // Implementation to book a flight based on the provided booking request
        return bookingService.bookFlight(request);
    }

    // Endpoint to cancel a booking for a user
    @DELETE("/bookings/{bookingId}")
    public void cancelBooking(@PathVariable Long bookingId) {
        // Implementation to cancel the booking with the provided ID
        bookingService.cancelBooking(bookingId);
    }

    // Endpoint to get all bookings for a user
    @GET("/users/{userId}/bookings")
    public List<Booking> getAllBookingsForUser(@PathVariable Long userId) {
        // Implementation to fetch and return all bookings for the provided user ID
        return bookingService.getAllBookingsForUser(userId)
    




}