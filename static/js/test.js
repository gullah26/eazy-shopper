const test = document.getElementById("test");

// This handler will be executed only once when the cursor
// moves over the unordered list
test.addEventListener("mouseenter", (event) => {
  // highlight the mouseenter target
  event.target.style.color = "purple";

  // reset the color after a short delay
  setTimeout(() => {
    event.target.style.color = "red";
  }, 500);
}, false);

// This handler will be executed every time the cursor
// is moved over a different list item
test.addEventListener("mouseover", (event) => {
  // highlight the mouseover target
  event.target.style.color = "orange";

  // reset the color after a short delay
  setTimeout(() => {
    event.target.style.color = "blue";
  }, 500);
}, false);
