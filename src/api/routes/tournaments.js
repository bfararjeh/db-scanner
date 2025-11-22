const express = require('express');
const router = express.Router();
const db = require('../../../db');

router.get('/index', async (req, res) => {
  try {
    const result = await db.query(`
      SELECT liquidpedia_url
      FROM tournament_index
    `);
    res.json(result.rows);
  } catch (err) {
    console.error('Error fetching tournament index:', err);
    res.status(500).json({ error: 'Internal server error' });
  }
});

module.exports = router;