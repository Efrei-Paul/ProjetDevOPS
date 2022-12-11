describe('Dashboard', () => {
  it('Checks if everything is in the page', () => {
    cy.visit('http://localhost:8501')
    cy.get('[id="prediction-de-prix-de-maison"]').should('exist')
    cy.get('[data-baseweb="input"]').should('exist')
  })
})