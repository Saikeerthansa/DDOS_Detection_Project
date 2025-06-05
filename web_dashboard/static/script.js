document.addEventListener("DOMContentLoaded", function () {
    const logTable = document.getElementById("logTable");
    const ctx = document.getElementById("attackChart").getContext("2d");

    // Initialize Chart
    let attackChart = new Chart(ctx, {
        type: "bar",
        data: {
            labels: [],
            datasets: [{
                label: "Attack Frequency",
                backgroundColor: "rgba(255, 0, 0, 0.6)",
                borderColor: "black",
                borderWidth: 1,
                data: []
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            animation: {
                duration: 1000,
                easing: 'easeInOutQuad'
            },
            scales: {
                x: {
                    ticks: { font: { size: 14 } }
                },
                y: {
                    beginAtZero: true,
                    ticks: { font: { size: 14 } }
                }
            }
        }
    });

    function fetchLogs() {
        fetch("/api/logs")
            .then(response => response.json())
            .then(logs => {
                logTable.innerHTML = "";
                logs.forEach(log => {
                    let row = `<tr><td>${log.timestamp}</td><td>${log.event}</td></tr>`;
                    logTable.innerHTML += row;
                });
            });
    }
    
    function fetchMaliciousIPs() {
        fetch("/api/malicious_ips")
            .then(response => response.json())
            .then(ips => {
                maliciousIpsTable.innerHTML = "";
                ips.forEach(ip => {
                    let row = `<tr><td>${ip}</td></tr>`;
                    maliciousIpsTable.innerHTML += row;
                });
            });
    }

    function fetchAttackData() {
        fetch("/api/attack_data")
            .then(response => response.json())
            .then(data => {
                attackChart.data.labels = Object.keys(data);
                attackChart.data.datasets[0].data = Object.values(data);
                attackChart.update();
            });
    }

    // Auto-refresh every 5 seconds
    setInterval(() => {
        fetchLogs();
        fetchMaliciousIPs();
        fetchAttackData();
    }, 5000);
});

