$("#id_mailing").on("click", function () {
	if ($("#id_mailing").is(":checked")) {
		$("#id_mailing").attr("value", "true");
	} else {
		$("#id_mailing").attr("value", "false");
	}
});
