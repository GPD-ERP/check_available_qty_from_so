frappe.ui.form.on('Sales Order', {
	setup(frm) {
        // your code here
            console.log('call')
				frm.set_indicator_formatter('item_code',
			function(doc) { return (doc.actual_qty>=doc.qty) ? "green" : "red" })
    }
})

frappe.ui.form.on('Sales Order Item', {
	qty(frm) {
        // your code here
        cur_frm.refresh_field("items")
    }
})