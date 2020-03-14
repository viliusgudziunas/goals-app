import faker from 'faker';

const email = faker.internet.email();
const password = faker.internet.password();

describe('Login', () => {
  it('should display the log in form', () => {
    cy.visit('/login')
      .get('h1')
      .contains('Log In')

      .get('form');
  });

  it('should allow a user to log in', () => {
    // register user
    cy.visit('/register')
      .get('input[name="email"]')
      .type(email)

      .get('input[name="password"]')
      .type(password)

      .get('button[type="submit"]')
      .click();

    // log a user out
    cy.get('a')
      .contains('Log Out')
      .click();

    // log a user in
    cy.get('a')
      .contains('Log In')
      .click()

      .get('input[name="email"]')
      .type(email)

      .get('input[name="password"]')
      .type(password)

      .get('button[type="submit"]')
      .click();

    // assert user is redirected to "/"
    // assert "/" is displayed properly
    cy.contains('All Users');

    cy.get('table')
      .find('tbody > tr')
      .last()
      .find('td')
      .contains(email);

    cy.get('.navbar-collapse').within(() => {
      cy.get('.nav-link')
        .contains('User Status')

        .get('.nav-link')
        .contains('Log Out')

        .get('.nav-link')
        .contains('Log In')
        .should('not.be.visible')

        .get('.nav-link')
        .contains('Register')
        .should('not.be.visible');
    });
  });
});
