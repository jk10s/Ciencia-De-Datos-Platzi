function Car (licene,driver) {
    this.id;
    this.licene = licene;
    this.driver = driver;
    this.passenger;
}

Car.prototype.imprime= function(){
    console.log(this.driver)
    console.log(this.driver.name)
    console.log(this.driver.document)
}