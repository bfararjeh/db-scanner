require('dotenv').config();
const express = require('express');
const app = express();
const PORT = process.env.PORT || 8000;


// ===== MIDDLEWARE =====
// allows for parsing of json files which is how api requests will be made
// .json() is the middleware were using
app.use(express.json());

// ===== ROUTES =====
// importing the different routes then mount them
const tournamentRoutes = require('./src/api/routes/tournaments');
app.use('/tournaments', tournamentRoutes);

// Base route
app.get('/', (req, res) => {
  res.send('uppercutsAPI is live');
});

// ===== START SERVER =====
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});