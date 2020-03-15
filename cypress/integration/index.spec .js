describe('Index', () => {
  it('should display the page correctly if a user is not logged in', () => {
    cy.visit('/')
      .get('h1')
      .contains('All Users');

    cy.get('.navbar-collapse').within(() => {
      cy.get('.nav-link')
        .contains('User Status')
        .should('not.be.visible')

        .get('.nav-link')
        .contains('Log Out')
        .should('not.be.visible')

        .get('.nav-link')
        .contains('Log In')

        .get('.nav-link')
        .contains('Register');
    });
  });
});
