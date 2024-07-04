// Copyright (c) 2024, Ahmed Reda and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Accounts"] = {
    "filters": [
        {
            fieldname: "parent_account",
            label: "Please Select Parent Account",
            fieldtype: "Link",
            options: "Account",
            width: "350px"
        },
        {
            fieldname: "account_name",
            label: "Please Select Account Name",
            fieldtype: "Link",
            options: "Account",
            width: "350px"
        }
    ],

    "formatter": function (value, row, column, data, default_formatter) {
        if (column.fieldname == "account_name") {
            value = data.account_name;
            column.is_tree = true;  // Indicate that this column is part of a tree structure

            // Optionally, set an onclick event for opening a detailed view if necessary
            column.link_onclick =
                "frappe.query_reports['Accounts'].open_profit_and_loss_statement(" +
                JSON.stringify(data) +
                ")";
        }

        value = default_formatter(value, row, column, data);

        if (!data.parent_account) {
            var $value = $("<span>").text(value).css("font-weight", "bold");
            if (data.warn_if_negative && data[column.fieldname] < 0) {
                $value.addClass("text-danger");
            }

            value = $value.wrap("<p></p>").parent().html();
			console.log("VALUE",value);
			console.log("data",data);
			console.log("column",column);
			console.log("rows",row);
			console.log("default_formatter",default_formatter);
        }

        return value;
    },

    "tree": true,
    "name_field": "account_name",
    "parent_field": "parent_account",
    "initial_depth": 3,
    

};

