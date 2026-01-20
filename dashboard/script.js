// Sample data
const data = {
    totalSales: 125000,
    activeUsers: 1250,
    pendingOrders: 45,
    salesData: [12000, 15000, 18000, 22000, 25000, 28000, 30000, 32000, 35000, 38000, 40000, 42000],
    usersData: [800, 900, 1000, 1100, 1150, 1200, 1220, 1240, 1250, 1260, 1270, 1280],
    orders: [
        { id: 1, cliente: 'Juan Pérez', producto: 'Producto A', monto: 150, estado: 'Completado' },
        { id: 2, cliente: 'María García', producto: 'Producto B', monto: 200, estado: 'Pendiente' },
        { id: 3, cliente: 'Carlos López', producto: 'Producto C', monto: 300, estado: 'Enviado' },
        { id: 4, cliente: 'Ana Rodríguez', producto: 'Producto A', monto: 150, estado: 'Completado' },
        { id: 5, cliente: 'Pedro Martínez', producto: 'Producto D', monto: 400, estado: 'Pendiente' }
    ]
};

// Populate cards
document.getElementById('total-sales').textContent = `$${data.totalSales.toLocaleString()}`;
document.getElementById('active-users').textContent = data.activeUsers.toLocaleString();
document.getElementById('pending-orders').textContent = data.pendingOrders;

// Populate table
const tableBody = document.getElementById('orders-table');
data.orders.forEach(order => {
    const row = document.createElement('tr');
    row.innerHTML = `
        <td>${order.id}</td>
        <td>${order.cliente}</td>
        <td>${order.producto}</td>
        <td>$${order.monto}</td>
        <td>${order.estado}</td>
    `;
    tableBody.appendChild(row);
});

// Sales Chart
const salesCtx = document.getElementById('salesChart').getContext('2d');
new Chart(salesCtx, {
    type: 'bar',
    data: {
        labels: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
        datasets: [{
            label: 'Ventas Mensuales',
            data: data.salesData,
            backgroundColor: 'rgba(54, 162, 235, 0.5)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

// Users Chart
const usersCtx = document.getElementById('usersChart').getContext('2d');
new Chart(usersCtx, {
    type: 'line',
    data: {
        labels: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
        datasets: [{
            label: 'Usuarios Activos',
            data: data.usersData,
            backgroundColor: 'rgba(75, 192, 192, 0.5)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

// PDF Generation
function generatePDF() {
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();

    // Title
    doc.setFontSize(20);
    doc.setTextColor(40, 40, 40);
    doc.text('Reporte del Dashboard', 20, 20);

    // Metrics
    doc.setFontSize(12);
    doc.setTextColor(0, 0, 0);
    doc.text(`Ventas Totales: $${data.totalSales.toLocaleString()}`, 20, 40);
    doc.text(`Usuarios Activos: ${data.activeUsers.toLocaleString()}`, 20, 50);
    doc.text(`Pedidos Pendientes: ${data.pendingOrders}`, 20, 60);

    // Table
    const tableData = data.orders.map(order => [order.id, order.cliente, order.producto, `$${order.monto}`, order.estado]);

    doc.autoTable({
        head: [['ID', 'Cliente', 'Producto', 'Monto', 'Estado']],
        body: tableData,
        startY: 80,
        theme: 'grid',
        headStyles: { fillColor: [54, 162, 235], textColor: 255 },
        alternateRowStyles: { fillColor: [245, 245, 245] },
        styles: { fontSize: 10 }
    });

    doc.save('reporte-dashboard.pdf');
}