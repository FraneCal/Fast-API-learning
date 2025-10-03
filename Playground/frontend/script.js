// When the button with id="loadBtn" is clicked, run this function
document.getElementById("loadBtn").onclick = async () => {

  // Send a GET request to your FastAPI endpoint /all-items
  const res = await fetch("http://127.0.0.1:8000/all-items");

  // Convert the response into JSON (your inventory dictionary)
  const data = await res.json();

  // Show a little status text below the button
  document.getElementById("status").innerText = "Loaded ✔";

  // Build HTML table rows from the data we got back
  let html = "";
  for (const id in data) {
    const item = data[id];   // each value is one inventory item
    html += `<tr>
              <td>${id}</td>              <!-- item ID -->
              <td>${item.name}</td>       <!-- item name -->
              <td>${item.price}</td>      <!-- item price -->
              <td>${item.brand}</td>      <!-- item brand -->
            </tr>`;
  }

  // Insert the built rows into the <tbody> of the table
  document.querySelector("#itemsTable tbody").innerHTML = html;

  // Make sure the table is visible (it starts hidden in HTML)
  document.getElementById("itemsTable").hidden = false;
};


document.getElementById("firstItem").onclick = async () => {
  const res = await fetch("http://127.0.0.1:8000/get-item/1");
  const data = await res.json();

  document.getElementById("status").innerText = "Loaded ✔";

  let html = "";
  for (const id in data) {
    const item = data[id];
    html += `<tr>
              <td>${id}</td>
              <td>${item.name}</td>
              <td>${item.price}</td>
              <td>${item.brand}</td>
            </tr>`;
  }
  document.querySelector("#itemsTable tbody").innerHTML = html;
  document.getElementById("itemsTable").hidden = false;
};