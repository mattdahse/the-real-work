/* The next session, as announced in the site header.

   Written from Matt's Google Calendar when a session is chronicled — see the
   "Next session" step in .claude/skills/real-work-chronicle/SKILL.md. Safe to hand-edit
   between recaps if the table moves.

   when       the next session's start, ALWAYS in Arizona time.
              Arizona keeps no daylight saving, so the offset is always -07:00.
              Format: 'YYYY-MM-DDTHH:MM:00-07:00'  (24-hour clock; 17:00 = 5 PM)
              Set to null to say plainly that nothing is on the books.
   mode       'in-person', 'online', or 'hybrid' (a table with someone dialling in).
              The crusade's table lets the weekday decide this (Friday online, Saturday in
              person). This table has not settled a rule yet — until it does, set the mode
              by hand from what Matt says, never from the calendar entry's title.
   where      optional — a room or a host's name. NEVER a meeting link or its passcode:
              this file is served on the public site.
   runsHours  how long the session runs, taken from the calendar event's own length.
              Until that much time has passed the header says the session is under way;
              after it, the date has gone stale and the header reports none scheduled.

   The page converts `when` into each reader's own local time, wherever they are. */

window.NEXT_SESSION = {
  when: null,
  mode: 'in-person',
  where: '',
  runsHours: 5
};
