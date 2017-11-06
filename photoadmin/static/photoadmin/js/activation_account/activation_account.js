/**
 * 
 */

function wizard_onStepChange(event, currentIndex, newIndex) {
	if (console) {
		console.log("wizard_onStepChange():: Enter");
		console.log("wizard_onStepChange():: event = "+event);
		console.log("wizard_onStepChange():: currentIndex = "+currentIndex);
		console.log("wizard_onStepChange():: newIndex = "+newIndex);
	}
	
	if (currentIndex == 0) {
		$("#facebook-hidden").val("https://www.facebook.com/"+$("#facebook-input").val());
	}
	
	return true;
}

function wizard_onFinished(event, currentIndex) {
	if (console) {
		console.log("wizard_onFinished():: Enter");
		console.log("wizard_onFinished():: event = "+event);
		console.log("wizard_onFinished():: currentIndex = "+currentIndex);		
	}
	
	$("#wizardForm").submit();
	return true
}

function wizard_onCancel(event){
	if (console) {
		console.log("wizard_onCancel():: Enter");
		console.log("wizard_onCancel():: event = "+event);		
	}	
	
	location.pathname = "/photoadmin";
	return true;
}
