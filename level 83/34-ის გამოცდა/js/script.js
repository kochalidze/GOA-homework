// 2) ჯავასკრიპტის პროგრამა (გასტილული) რომელსაც აქვს 
//    ორი შესაყვანი ველი- ( გადასახადი, "tip" ) და გამოითლის შესაბამის რიცხვს


function calculateTip() {

    const billAmount = parseFloat(document.getElementById('billAmount').value);
    const tipPercent = parseFloat(document.getElementById('tipPercent').value);
    

    if (isNaN(billAmount) || isNaN(tipPercent)) {
        document.getElementById('result').innerText = "Please enter valid numbers!";
        return;
    }
    
    const tipAmount = (billAmount * tipPercent) / 100;
    const totalAmount = billAmount + tipAmount;
    
    document.getElementById('result').innerText = `Tip: $${tipAmount.toFixed(2)} | Total: $${totalAmount.toFixed(2)}`;
}
calculateTip()
